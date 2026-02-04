import os
import glob

# Get all image files
image_extensions = ['*.jpg', '*.jpeg', '*.png']
images = []
for ext in image_extensions:
    images.extend(glob.glob(os.path.join('.', '**', ext), recursive=True))

# Remove leading ./
images = [img[2:] for img in images]

# Base URL
base_url = 'https://trainingcontentteam.github.io/Lexipol_Assets/'

# Generate HTML
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lexipol Assets Image Grid</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        header {
            background-color: #007acc;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .search-container {
            margin-bottom: 20px;
        }
        #search {
            width: 100%;
            max-width: 400px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .item {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            overflow: hidden;
            transition: transform 0.2s;
        }
        .item:hover {
            transform: translateY(-5px);
        }
        img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .info {
            padding: 15px;
            text-align: center;
        }
        .filename {
            font-weight: bold;
            margin-bottom: 10px;
        }
        .folder {
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
        }
        button {
            background-color: #007acc;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        button:hover {
            background-color: #005a9e;
        }
    </style>
</head>
<body>
    <header>
        <h1>Lexipol Assets Image Gallery</h1>
        <div class="search-container">
            <input type="text" id="search" placeholder="Search by filename, folder, or metadata...">
        </div>
    </header>
    <div class="grid" id="grid">
'''

for img in sorted(images):
    url = base_url + img.replace(' ', '%20')
    filename = os.path.basename(img)
    folder = os.path.dirname(img)
    html += f'''
        <div class="item" data-filename="{filename.lower()}" data-folder="{folder.lower()}" data-url="{url.lower()}">
            <img src="{url}" alt="{filename}">
            <div class="info">
                <div class="filename">{filename}</div>
                <div class="folder">Folder: {folder}</div>
                <button onclick="navigator.clipboard.writeText('{url}')">Copy URL</button>
            </div>
        </div>
'''

html += '''
    </div>
    <script>
        const searchInput = document.getElementById('search');
        const items = document.querySelectorAll('.item');

        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            items.forEach(item => {
                const filename = item.dataset.filename;
                const folder = item.dataset.folder;
                const url = item.dataset.url;
                if (filename.includes(query) || folder.includes(query) || url.includes(query)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html)

print("index.html generated")