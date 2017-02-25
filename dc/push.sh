
#!/usr/bin/env bash

APP_PATH="$HOME/dc"

echo "Open the app directory"
cd $APP_PATH
echo "Pulling source code..."
git clean -f
git pull
echo "Finished"
