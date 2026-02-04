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
    <title>Lexipol Assets Image Gallery</title>
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
        .filters {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            align-items: center;
        }
        #copyAll {
            padding: 10px 16px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f0f0f0;
            cursor: pointer;
        }
        #copyAll:hover {
            background-color: #e0e0e0;
        }
        #search, #folderSelect {
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            min-width: 200px;
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
        .buttons {
            display: flex;
            gap: 10px;
            justify-content: center;
        }
        .download-btn {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            text-decoration: none;
            display: inline-block;
            transition: background-color 0.2s;
        }
        .download-btn:hover {
            background-color: #218838;
        }
        .loading {
            text-align: center;
            padding: 50px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Lexipol Assets Image Gallery</h1>
        <div class="filters">
            <input type="text" id="search" placeholder="Search by filename...">
            <select id="folderSelect">
                <option value="">All Folders</option>
            </select>
            <button id="copyAll">Copy All URLs in Folder</button>
        </div>
    </header>
    <div class="loading">Loading images...</div>
    <div class="grid" id="grid">
    </div>
    <script>
        const searchInput = document.getElementById('search');
        const folderSelect = document.getElementById('folderSelect');
        const grid = document.getElementById('grid');
        const loading = document.querySelector('.loading');
        let allImages = [];
        let folders = new Set();

        async function fetchImages() {
            try {
                const response = await fetch('https://api.github.com/repos/TrainingContentTeam/Lexipol_Assets/contents');
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                const data = await response.json();
                console.log('Root data:', data);
                const imagePromises = [];

                for (const item of data) {
                    if (item.type === 'dir') {
                        folders.add(item.name);
                        imagePromises.push(fetchFolderImages(item.path));
                    }
                }

                const imageArrays = await Promise.all(imagePromises);
                allImages = imageArrays.flat();
                console.log('All images:', allImages);

                populateFolderDropdown();
                displayImages();
                loading.style.display = 'none';
            } catch (error) {
                console.error('Error fetching images:', error);
                loading.textContent = 'Error loading images: ' + error.message + '. Check console for details.';
            }
        }

        async function fetchFolderImages(path) {
            try {
                const encodedPath = encodeURIComponent(path);
                const response = await fetch(`https://api.github.com/repos/TrainingContentTeam/Lexipol_Assets/contents/${encodedPath}`);
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status} for ${path}: ${response.statusText}`);
                }
                const data = await response.json();
                console.log(`Data for ${path}:`, data);
                return data.filter(item => item.type === 'file' && ['jpg', 'jpeg', 'png'].some(ext => item.name.toLowerCase().endsWith('.' + ext))).map(item => ({
                    url: item.download_url,
                    path: item.path,
                    name: item.name.replace(/`/g, '\\`'),
                    folder: path.replace(/`/g, '\\`')
                }));
            } catch (error) {
                console.error(`Error fetching folder ${path}:`, error);
                return []; // Return empty array on error
            }
        }

        function populateFolderDropdown() {
            folders.forEach(folder => {
                const option = document.createElement('option');
                option.value = folder;
                option.textContent = folder;
                folderSelect.appendChild(option);
            });
        }

        function displayImages() {
            grid.innerHTML = '';
            const searchQuery = searchInput.value.toLowerCase();
            const selectedFolder = folderSelect.value;

            allImages.forEach(img => {
                if ((selectedFolder === '' || img.folder === selectedFolder) &&
                    (searchQuery === '' || img.name.toLowerCase().includes(searchQuery))) {
                    const item = document.createElement('div');
                    item.className = 'item';
                    item.innerHTML = `
                        <img src="${img.url}" alt="${img.name}">
                        <div class="info">
                            <div class="filename">${img.name}</div>
                            <div class="folder">Folder: ${img.folder}</div>
                            <div class="buttons">
                                <button onclick="navigator.clipboard.writeText('${img.url}')">Copy URL</button>
                                <a href="${img.url}" download="${img.name}" class="download-btn">Download</a>
                            </div>
                        </div>
                    `;
                    grid.appendChild(item);
                }
            });
        }

        searchInput.addEventListener('input', displayImages);
        folderSelect.addEventListener('change', displayImages);

        document.getElementById('copyAll').addEventListener('click', function() {
            const selectedFolder = folderSelect.value;
            if (selectedFolder === '') {
                alert('Please select a specific folder to copy URLs.');
                return;
            }
            const folderImages = allImages.filter(img => img.folder === selectedFolder);
            const text = folderImages.map(img => `${img.name}: ${img.url}`).join('\n');
            navigator.clipboard.writeText(text).then(() => {
                alert(`Copied ${folderImages.length} URLs to clipboard.`);
            }).catch(err => {
                console.error('Failed to copy: ', err);
                alert('Failed to copy URLs.');
            });
        });

        fetchImages();
    </script>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html)

print("index.html generated")