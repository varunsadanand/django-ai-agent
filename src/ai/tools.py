# ai/tools.py
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from docs.models import Document

@tool
def list_documents(config:RunnableConfig):
    """             
    Retrieve all active documents from the database.
    Returns a list of dictionaries containing document metadata.
    """
    print(config)
    metadata=config.get('configurable') or config.get('metadata')
    user_id=metadata.get('user_id')
    qs = Document.objects.filter(active=True)
    response_data = []

    for doc in qs:
        response_data.append({
            "id": doc.id,
            "title": doc.title,
        })

    return response_data


@tool
def get_document(doc_id: int,config:RunnableConfig):
    """
    Retrieve a single document by its ID.
    """
    metadata=config.get('configurable') or config.get('metadata')
    user_id=metadata.get('user_id')
    if user_id is None:
        raise Exception("User not found ")
    try:
        doc = Document.objects.get(id=doc_id,owner_id=user_id, active=True)
    except Document.DoesNotExist:
        return {"error": "Document not found"}
    except:
        raise Exception("invalid request for document")
    response_data= {
            "id": doc.id,
            "title": doc.title,
        }
