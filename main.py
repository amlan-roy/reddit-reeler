from generateVideo import MusicCategory, makeVideo
        
def main():
    makeVideo(audioVolume=1.5,
        bgMusicType=MusicCategory.commentry
        )

if __name__ == "__main__":
    main()