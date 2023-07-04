from pathlib import Path
from read_files import ReadContents

class ScanDocument:
    """ 
    The class calls the read files module to access the various file types supported by the module.
    """
    read_contents = ReadContents()
    
    def __init__(self):
        self.__all_file_names = []
        self.store_file_names() # Populates file names only once.

    
    @classmethod
    def get_docs(cls)-> Path:
        """Prompts the user for a directory containing only the files to scan/read."""

        cls.dir_path = input("Directory: ").strip()

        while True:
            cls.src_dir = Path(cls.dir_path)
            if cls.src_dir.is_dir(): # If provided path exists in the OS.
                return cls.src_dir
            else:
                cls.dir_path = input("Invalid directory. Please enter a valid directory: ").strip()

        

    def get_files(self):
        """Retrieves exclusively the files located in the returned directory by the getdoc() function."""
        self.get_docs()

        self.present_files = [(files.name, files.suffix) for files in self.src_dir.iterdir() if files.is_file()]
        print("Files in Root Directory:", )

        self.ext = {}
        for file_name, file_extension in self.present_files:
            print(file_name, end= ", ") # File names
            self.ext[file_extension] = self.ext.get(file_extension, 0) + 1 # File extensions.

        print("\n")
        print(f"Extensions:\n{self.ext}")

    @property
    def all_file_names(self): # To avoid modification of the list.
        return self.__all_file_names
    
    def store_file_names(self):
        self.get_files()

        for file_name, file_extension in self.present_files:
            self.__all_file_names.append(file_name)

    def choose_file_type(self):
        
        self.all_file_names
        self.pick_type = input("Which file type(s) do you want to scan? ").strip().lower()

        if self.pick_type == ".txt": # Read .txt files
            self.txt_files = filter(lambda file_name: file_name.endswith('.txt'), self.all_file_names)
            print(list(self.txt_files)) # Counter the filter object returned 0by txt_files

            self.read_contents.read_txt(files_src= self.src_dir, files_present= self.present_files)





        


def main():
    scan_document = ScanDocument()

    scan_document.choose_file_type()
    

if __name__ == "__main__":
    main()