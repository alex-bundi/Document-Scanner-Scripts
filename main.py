from pathlib import Path

class ScanDocument:
    """ 
    The class calls the read files module to access the various file types supported by the module.
    """

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
            self.ext[file_extension] = self.ext.get(file_extension, 0) + 1 # File extensions

        print("\n")
        print(f"Extensions:\n{self.ext}")





        


def main():
    scan_document = ScanDocument()
    scan_document.get_files()

if __name__ == "__main__":
    main()