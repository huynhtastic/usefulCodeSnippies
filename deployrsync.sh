# Command to use rsync to deploy only changes between a source and destination directory, similar to intellij's
# deployment/upload-to function

rsync -avP --delete --exclude '.git/*' 'source' 'dest'
