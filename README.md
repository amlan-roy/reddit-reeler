# Reddit Reeler <img width="35" alt="under construction image" src="https://user-images.githubusercontent.com/59330872/205681390-d8622243-b0b0-4a8e-9443-b9d3a4c527f6.png">  [UNDER CONSTRUCTION]

- An UNDER CONSTRUCTION web app which makes read-out-loud videos of reddit posts.
- This app has gone through many iterations, but the current version has the following flow:
  - Upload screenshots which will be used as images
  - Text will be extracted from the images. Manually correct minor changes in the generated texts.
  - A read-out-loud video will be generated with a random bg and music.
- Python is used as the main driver code for text extraction, audio generation and image/video manupulation.
- React is used for the frontend [UNDER CONSTRUCTION]

## Text Extraction
- Tesseract OCR is used for Text detection.
- Installation and setup guide for tesseract OCR: 
  - https://github.com/tesseract-ocr/tesseract
  - https://github.com/UB-Mannheim/tesseract/wiki
 
## Audio Generation
 - Two modules are used audio gen: pyttsx3 and gtts
 
## Video Generation
 - Moviepy is used for video generation

## Image Generation (Deprecated)
- Pillow (PIL) used for image generation
- This is not used now. This was used in earlier versions for generating images from reddit post links


THIS PROJECT IS NOWHERE NEAR COMPLETION.
Feel free to contribute and/or use this for your own projects.
