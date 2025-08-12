#!/bin/bash

# Release script

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Usage: ./release.sh <version>"
    exit 1
fi

echo "Releasing version $VERSION..."

# Update version file
echo $VERSION > VERSION

# Update changelog
echo "Please update CHANGELOG.md manually"

# Commit changes
git add -A
git commit -m "Release v$VERSION"

# Create tag
git tag -a "v$VERSION" -m "Release version $VERSION"

# Push changes
echo "Ready to push. Run:"
echo "  git push origin main"
echo "  git push origin v$VERSION"

echo "Release prepared!"