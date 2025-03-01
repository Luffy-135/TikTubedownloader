# import os
# import yt_dlp

# def create_folder():
#     folder_name = input("Enter folder name: ")
#     folder_path = f"/storage/emulated/0/{folder_name}"
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)
#         print(f"✅ Folder '{folder_name}' created successfully!")
#     else:
#         print(f"⚠️ Folder '{folder_name}' already exists!")
#     return folder_path

# def download_video(url, output_folder, format_option, quality):
#     ydl_opts = {
#         'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
#     }
    
#     if format_option == "2":
#         ydl_opts['format'] = 'bestaudio/best'
#         ydl_opts['postprocessors'] = [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }]
#     else:
#         ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best'

#     print("⏳ Downloading...")
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         print("✅ Download completed successfully!")
#     except Exception as e:
#         print(f"❌ Error: {e}")

# def check_downloads(folder_path):
#     files = os.listdir(folder_path)
#     if files:
#         print("\n📂 Downloaded Files:")
#         for file in files:
#             print(f" - {file}")
#     else:
#         print("⚠️ No downloaded files found!")

# def main():
#     while True:
#         print("\n==========******************=========")
#         print(" TOOL DOWNLOADER TIKTOK AND YOUTUBE")
#         print(" CREATE BY: PHIROM ")
#         print("==========******************=========")
#         print("[1] Create Folder")
#         print("[2] Paste URL Link")
#         print("[3] Input Folder: /storage/emulated/0/My file")
#         print("[4] Choose Format: 1. MP4, 2. MP3")
#         print("[5] Choose Quality: 144p, 240p, 360p, 480p, 720p, 1080p, 2K, 4K, 8K")
#         print("[6] Start Download")
#         print("[7] Stop Download")
#         print("[8] Check Download Success")
#         print("[9] Exit")
#         print("==========***=========")
#         choice = input("Choose: ")

#         if choice == "1":
#             output_folder = create_folder()
#         elif choice == "2":
#             url = input("Paste the video URL: ")
#         elif choice == "3":
#             output_folder = "/storage/emulated/0/My file"
#             print(f"✅ Output folder set to: {output_folder}")
#         elif choice == "4":
#             format_option = input("Choose format (1. MP4, 2. MP3): ")
#         elif choice == "5":
#             quality = input("Choose video quality (144, 240, 360, 480, 720, 1080, 2K, 4K, 8K): ")
#         elif choice == "6":
#             if not url or not output_folder or not format_option or not quality:
#                 print("⚠️ Please complete all steps before starting the download!")
#             else:
#                 download_video(url, output_folder, format_option, quality)
#         elif choice == "7":
#             print("🚫 Stop download feature is not implemented yet!")
#         elif choice == "8":
#             check_downloads(output_folder)
#         elif choice == "9":
#             print("👋 Exiting... Goodbye!")
#             break
#         else:
#             print("⚠️ Invalid choice! Please try again.")

# if __name__ == "__main__":
#     os.system("termux-setup-storage")  # Ensure Termux has storage access
#     main()


import os
import yt_dlp

def create_folder():
    folder_name = input("Enter folder name: ")
    folder_path = f"/storage/emulated/0/{folder_name}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ Folder '{folder_name}' created successfully!")
    else:
        print(f"⚠️ Folder '{folder_name}' already exists!")
    return folder_path

def download_video(urls, output_folder, format_option, quality):
    for url in urls:
        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
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
                ydl.download([url])
            print("✅ Download completed successfully!")
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")
            print("➡️ Skipping to the next video...")

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
        print("[3] Input Folder: /storage/emulated/0/My file")
        print("[4] Choose Format: 1. MP4, 2. MP3")
        print("[5] Choose Quality: 144p, 240p, 360p, 480p, 720p, 1080p, 2K, 4K, 8K")
        print("[6] Start Download")
        print("[7] Stop Download")
        print("[8] Check Download Success")
        print("[9] Exit")
        print("==========***=========")
        choice = input("Choose: ")

        if choice == "1":
            output_folder = create_folder()
        elif choice == "2":
            url = input("Paste the video URL: ")
            if url:
                urls.append(url)
        elif choice == "3":
            output_folder = "/storage/emulated/0/My file"
            print(f"✅ Output folder set to: {output_folder}")
        elif choice == "4":
            format_option = input("Choose format (1. MP4, 2. MP3): ")
        elif choice == "5":
            quality = input("Choose video quality (144, 240, 360, 480, 720, 1080, 2K, 4K, 8K): ")
        elif choice == "6":
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
        elif choice == "7":
            print("🚫 Stop download feature is not implemented yet!")
        elif choice == "8":
            check_downloads(output_folder)
        elif choice == "9":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    os.system("termux-setup-storage")  # Ensure Termux has storage access
    main()
