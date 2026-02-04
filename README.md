# ⚠️ IMPORTANT WARNING ⚠️

**Changes to image files in this repository will directly affect live courses in our LMS.** Any modifications, deletions, or renames of images may break course content that references these assets. Always coordinate with the course development team before making changes to existing images.

# Lexipol Assets Repository

This repository serves as a centralized storage for images used in our course content within the Learning Management System (LMS). The images and their URLs are referenced and copied for use in interactive elements built into our courses.

## Image Gallery

An interactive image gallery is available at: [https://trainingcontentteam.github.io/Lexipol_Assets/](https://trainingcontentteam.github.io/Lexipol_Assets/)

### Features
- **Dynamic Loading**: The gallery automatically discovers and displays all images from the repository folders using GitHub's API. No manual updates needed when adding new images.
- **Search Functionality**: Search images by filename using the search bar.
- **Folder Filtering**: Use the dropdown to filter images by specific folders.
- **Copy URLs**: Each image has a "Copy URL" button to easily copy the direct link for use in course content.
- **Responsive Design**: Modern, card-based layout that works on desktop and mobile devices.

### How to Use
1. Visit the gallery URL above.
2. Use the search bar to find images by filename.
3. Select a folder from the dropdown to narrow down results.
4. Click "Copy URL" on any image to get its direct link.
5. Paste the URL into your course content or interactive elements.

## Adding New Images

1. **Organize by Folders**: Create or use existing folders to categorize images (e.g., "Fall Protection images", "FF-Fire_Behavior-Images").
2. **Upload Images**: Add your image files (JPG, PNG, JPEG) to the appropriate folder.
3. **Commit and Push**: The gallery will automatically detect and display new images on the next page load.
4. **Supported Formats**: Only JPG, PNG, and JPEG files are displayed in the gallery.

## Repository Structure

- `Fall Protection images/`: Images related to fall protection training
- `FF-Fire_Behavior-Images/`: Images for fire behavior training
- `index.html`: The gallery webpage (auto-generated)
- `generate_html.py`: Script for generating the gallery (legacy, no longer needed)
- `README.md`: This file

## Technical Notes

- The gallery uses GitHub Pages for hosting and GitHub API for dynamic content loading.
- Images are served directly from GitHub's CDN for fast loading.
- No authentication required - the repository is public for easy access.
- For any issues with the gallery, check browser console for API errors.

## Contact

For questions about image usage or repository changes, contact the Training Content Team.
