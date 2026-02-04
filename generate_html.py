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
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .item {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        button {
            margin-top: 10px;
            padding: 5px 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Lexipol Assets Images</h1>
    <div class="grid">
'''

for img in sorted(images):
    url = base_url + img.replace(' ', '%20')
    html += f'''
        <div class="item">
            <img src="{url}" alt="{os.path.basename(img)}">
            <button onclick="navigator.clipboard.writeText('{url}')">Copy URL</button>
        </div>
'''

html += '''
    </div>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html)

print("index.html generated")