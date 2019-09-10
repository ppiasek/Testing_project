from Handlers.API import GDriveAPI

test = GDriveAPI()
test.print_list_files()
test.simple_upload("/home/xantek/Code/Python/Testing_project/Handlers/example_of_list_full_response.log", metadata={"name" : "test.log"})
test.download("1Rg1FCAuvx3Qai0r4UxZ5r_0fzTJHEWKz", dest="/home/xantek/Code/Python/Testing_project/DataExamples/Downloaded_data/test.exe")

print("Stop")