import os
def analyze_file_type(filename):
    extension=os.path.splitext(filename)[1].lower()
    image_extensions=['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    document_extensions=['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx']
    audio_extensions = ['.mp3', '.wav', '.aac', '.flac'] 
    archive_extensions = ['.zip', '.rar', '.tar', '.gz']  
    video_extensions = ['.mp4', '.avi', '.mov']           
    code_extensions = ['.py', '.html', '.css', '.js', '.cpp']
    if extension in image_extensions:
        return "Image"
    elif extension in document_extensions:
        return "Document"
    elif extension in audio_extensions:
        return "Audio"
    elif extension in video_extensions:
        return "Video"
    elif extension in archive_extensions:
        return "Archive"
    elif extension in code_extensions:
        return "Code"
    else:
        return "Other"
