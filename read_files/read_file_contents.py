import pathlib
#x = {"filename": "file1.txt", "page_no": 1, "content": "Lorem ipsum dolor sit amet."}

class ReadContents: 

    def read_txt(self, files_src, files_present):
        """Only reads documents with the file extension .txt"""
        self.files_src = files_src
        self.files_present = files_present

        for file_name, file_ext in self.files_present:
            if file_ext == ".txt":
                self.full_path = pathlib.PurePath(self.files_src, file_name) # To avoid FileNotFoundError
                with open(self.full_path, "r") as scanned_file:
                    self.data = scanned_file.read()
                    #print(self.data)
