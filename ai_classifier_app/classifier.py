import os
def analyze_file_type(filename):
    extension=os.path.splitext(filename)[1].lower()
    image_extensions=['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    document_extensions=['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx']
    audio_extensions = ['.mp3', '.wav', '.aac', '.flac']
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv']
    if extension in image_extensions:
        return "image"
    elif extension in document_extensions:
        return "Document"
    elif extension in audio_extensions:
        return "Audio"
    elif extension in video_extensions:
        return "Video"
    else:
        return "unknown"
if __name__=="__main__":
    print("Testing logic....")
    print(f"photo.png   -> {analyze_file_type('photo.png')}")
    print(f"notes.txt   -> {analyze_file_type('notes.txt')}")
    print(f"music.mp3   -> {analyze_file_type('music.mp3')}")

    
    