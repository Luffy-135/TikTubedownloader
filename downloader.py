import os
import yt_dlp
import time

def create_folder():
    folder_name = input("Enter folder name: ")
    folder_path = f"/storage/emulated/0/{folder_name}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ Folder '{folder_name}' created successfully!")
    else:
        print(f"⚠️ Folder '{folder_name}' already exists!")
    return folder_path

def sanitize_filename(filename):
    # Truncate filename to avoid too long names
    max_length = 100
    if len(filename) > max_length:
        filename = filename[:max_length]
    return filename

def download_video(urls, output_folder, format_option, quality):
    for url in urls:
        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'retries': 3,  # Retry up to 3 times
        }
        
        if format_option == "2":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best'

        print(f"⏳ Downloading {url}...")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                title = info_dict.get('title', 'video')
                sanitized_title = sanitize_filename(title)
                ydl_opts['outtmpl'] = f'{output_folder}/{sanitized_title}.%(ext)s'
                ydl.download([url])
            print("✅ Download completed successfully!")
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")
            print("➡️ Skipping to the next video...")
        time.sleep(5)  # Add a delay to avoid rate-limiting

def check_downloads(folder_path):
    if not folder_path:
        print("⚠️ No folder selected!")
        return
    
    files = os.listdir(folder_path)
    if files:
        print("\n📂 Downloaded Files:")
        for file in files:
            print(f" - {file}")
    else:
        print("⚠️ No downloaded files found!")

def main():
    urls = []
    output_folder = None
    format_option = None
    quality = None
    
    while True:
        print("\n==========******************=========")
        print(" TOOL DOWNLOADER TIKTOK AND YOUTUBE")
        print(" CREATE BY: PHIROM ")
        print("==========******************=========")
        print("[1] Create Folder")
        print("[2] Paste URL Link") 
        print("[3] Choose Format: 1. MP4, 2. MP3")
        print("[4] Choose Quality: 144p, 240p, 360p, 480p, 720p, 1080p, 2K, 4K, 8K")
        print("[5] Start Download")
        print("[6] Check Download Success")
       
        print("[0] Exit")
        print("==========***=========")
        choice = input("Choose: ")

        if choice == "1":
            output_folder = create_folder()
        elif choice == "2":
            url = input("Paste the video URL: ")
            if url:
                urls.append(url)
        elif choice == "3":
            format_option = input("Choose format (1. MP4, 2. MP3): ")
            if format_option not in ["1", "2"]:
                print("⚠️ Invalid format option! Please choose 1 for MP4 or 2 for MP3.")
                format_option = None
        elif choice == "4":
            quality = input("Choose video quality (144, 240, 360, 480, 720, 1080, 2K, 4K, 8K): ")
            if quality not in ["144", "240", "360", "480", "720", "1080", "2K", "4K", "8K"]:
                print("⚠️ Invalid quality option! Please choose a valid quality.")
                quality = None
        elif choice == "5":
            if not urls:
                print("⚠️ Please add at least one video URL!")
            elif not output_folder:
                print("⚠️ Please select an output folder!")
            elif not format_option:
                print("⚠️ Please choose a format!")
            elif not quality:
                print("⚠️ Please choose a video quality!")
            else:
                download_video(urls, output_folder, format_option, quality)
                urls.clear()
        elif choice == "6":
            check_downloads(output_folder)
        elif choice == "0":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    os.system("termux-setup-storage")  # Ensure Termux has storage access
    main()