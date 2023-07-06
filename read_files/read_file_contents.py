import pathlib
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