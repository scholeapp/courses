If generated AA video is too heavy, you can compress with

`ffmpeg -i input.mp4  -vcodec libx265 -crf 28 output.mp4`

For MacOs, you need to preserve compatibility encoding H.265/HEVC for QuickTime:

`ffmpeg -i input.mp4   -c:v libx265 -preset fast -crf 28 -tag:v hvc1 -c:a eac3 -b:a 224k  output.mp4`


[source](https://gist.github.com/lukehedger/277d136f68b028e22bed?permalink_comment_id=4181610#gistcomment-4181610)