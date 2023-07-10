import pathlib
import docx

#x = {"filename": "file1.txt", "page_no": 1, "content": "Lorem ipsum dolor sit amet."}

class ReadContents: 

    def read_txt(self, files_src, files_present):
        """Only reads documents with the file extension .txt"""

        self.files_src = files_src
        self.files_present = files_present
        self.txt_lines = []

        for file_name, file_ext in self.files_present:
            if file_ext == ".txt":
                self.txt_info = {}
                self.full_path = pathlib.PurePath(self.files_src, file_name) # To avoid FileNotFoundError
                with open(self.full_path, "r") as scanned_file:
                    self.content = scanned_file.read()
                    self.txt_info["filename"] = file_name
                    self.txt_info["content"] = self.content.replace("\n", "").lower()
                self.txt_lines.append(self.txt_info)        
        return self.txt_lines
    
    def read_docx(self, files_src, files_present):
        """Only reads .docx documents."""

        self.files_src = files_src
        self.files_present = files_present
        self.docx_info = {}

        for file_name, file_ext in self.files_present:
            
            if file_ext == ".docx":
                self.full_path = pathlib.PurePath(self.files_src, file_name) # To avoid FileNotFoundError
                doc = docx.Document(self.full_path) # Read .docx files

                if file_name in self.docx_info:
                # File name already exists, update content
                    self.docx_info[file_name]['content'] = doc
                else:
                    # File name doesn't exist, add file name and content
                    self.docx_info[file_name] = {
                        'content': doc
                    }

                if len(doc.tables) == 0:
                    for paragraphs in doc.paragraphs:
                        self.docx_info["content"] = paragraphs.text
                        print(self.docx_info)
                        
                else:
                     for table in doc.tables: # Access cells within the table
                        for row in table.rows:
                            for cell in row.cells:
                                self.text = cell.text.replace('\n', '').strip()
                                self.docx_info["content"] = self.text


