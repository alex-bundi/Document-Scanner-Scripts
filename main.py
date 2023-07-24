from pathlib import Path
from read_files import ReadContents

class ScanDocument:
    """ 
    The class calls the read files module to access the various file types supported by the module.
    """
    read_contents = ReadContents()
    
    def __init__(self) -> None:
        self.__all_file_names = []
        self.store_file_names() # Populates file names only once.

    
    @classmethod
    def get_docs(cls):
        """Prompts the user for a directory containing only the files to scan/read."""

        cls.dir_path = input("Directory: ").strip()
        cls.attempts = 0
        cls.max_attempts = 5

        while True:
            if len(cls.dir_path) != 0:
                cls.src_dir = Path(cls.dir_path)
                if cls.src_dir.is_dir():  # If provided path exists in the OS.
                    return cls.src_dir
            elif cls.attempts == cls.max_attempts:
                raise ValueError("Exceeded maximum number of attempts. Unable to find a valid directory or input is invalid.")

            cls.dir_path = input("Invalid directory. Please enter a valid directory: ").strip()
            cls.attempts += 1     

    def get_files(self) -> None:
        """Retrieves exclusively the files located in the returned directory by the getdoc() function."""
        self.get_docs()

        self.present_files = [(files.name, files.suffix) for files in self.src_dir.iterdir() if files.is_file()]
        print("Files in Root Directory:", )

        self.ext = {}
        for file_name, file_extension in self.present_files:
            print(file_name, end= ", ") # File names
            self.ext[file_extension] = self.ext.get(file_extension, 0) + 1 # File extensions.

        print("\n")
        print(f"Extensions:\n{self.ext}\n")

    @property
    def all_file_names(self): # To avoid modification of the list.
        return self.__all_file_names
    
    def store_file_names(self) -> None:
        """Stores all file names in specified directory."""

        self.get_files()

        for file_name, file_extension in self.present_files:
            self.__all_file_names.append(file_name)

    def file_type_filter(self, ftype):
        """"Filters functionality for files in specified directory according to their file extension."""
        self.ftype = ftype
        self.filters = filter(lambda file_name: file_name.endswith(self.ftype), self.all_file_names)
        return self.filters

    def choose_file_type(self):
        """ Gets input on which file type extension to scan and returns the specified file type extension."""
        
        self.all_file_names
        self.supported_ext = [".txt", ".docx", ".pdf"]
        self.pick_type = input("Which file type(s) do you want to scan? (.txt, .docx, .pdf) ").strip().lower()

        while True:
            if self.pick_type in self.supported_ext:

                if self.pick_type == ".txt": # Read .txt files
                    self.txt_files = self.file_type_filter(ftype= ".txt")
                    print(f"{list(self.txt_files)}\n") # Counter the filter object returned by txt_files
                    self.txt_data = self.read_contents.read_txt(files_src= self.src_dir, files_present= self.present_files)
                    return self.txt_data
                
                elif self.pick_type == ".docx":
                    self.docx_files = self.file_type_filter(ftype= ".docx")
                    print(f"{list(self.docx_files)}\n")
                    self.docx_data = self.read_contents.read_docx(files_src= self.src_dir, files_present= self.present_files)
                    return self.docx_data
                
                elif self.pick_type == ".pdf":
                    self.pdf_files = self.file_type_filter(ftype= ".pdf")
                    print(f"{list(self.pdf_files)}\n")
                    self.pdf_data = self.read_contents.read_pdf(files_src= self.src_dir, files_present= self.present_files)
                    return self.pdf_data
            
            else:
                self.pick_type = input("Invalid extension type; try again. Which file types do you want to scan? ").strip().lower()
                pass


def main():
    scan_document = ScanDocument()
    scan_document.choose_file_type()

if __name__ == "__main__":
    main()