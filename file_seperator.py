import os , shutil
# import pdb
dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document_extensions' : ('.doc', '.pdf', '.txt', '.docx','.pptx'),
    'image_extension' : ('.JPG','.JPEG','.GIF','.TIFF','.PSD','.EPS','.AI','.INDD','.RAW', '.png', '.jpg','.jpeg')
}

folder_path = input('enter folder path: ')

def file_finder(folder_path, file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

# print(file_finder(folder_path, video_extensions))

# pdb.set_trace()
for extension_type , extension_tuple in dict_extensions.items():
    # print('\nTHESE ARE YOUR SEPRATED FILES')
    # print(file_finder(folder_path, extension_tuple))
    folder_name = extension_type.split('_')[0] + 'Files'
    folderpath = os.path.join(folder_path, folder_name)
    os.mkdir(folderpath)
    for item in file_finder(folder_path, extension_tuple):
        item_path = os.path.join(folder_path, item)
        item_new_path = os.path.join(folderpath, item)
        shutil.move(item_path, item_new_path)
print('TASK COMPLETED!!!!\nGO TO FILE MANAGER AND CHECK THE PATH YOU ENTERED YOUR FOLDERS ARE CREATED!!!!!')