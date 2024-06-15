from win32com import client as win32

def extract_document_metadata(file_path):
    try:
        app = win32.Dispatch("Excel.Application")
        doc = app.Workbooks.Open(file_path, ReadOnly=True)
        metadata = doc.BuiltInDocumentProperties
        for prop in metadata:
            print(f"{prop}: {metadata[prop]}")
        doc.Close(False)
        app.Quit()
    except Exception as e:
        print(f"Failed to extract document metadata: {str(e)}")

# Example usage
file_path = "C:\\Users\\Administrator\\Pictures\\CIA triad.png"
extract_document_metadata(file_path)