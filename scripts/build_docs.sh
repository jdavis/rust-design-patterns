#!/bin/sh

# Set our variables
DOC_BRANCH="gh-pages"
DOCS_DIR="docs/"
SITE_DIR="_site/"
PLUGINS_DIR="$DOCS_DIR/_plugins/"
LAYOUTS_DIR="$DOCS_DIR/_layouts/"

function usage() {
    echo Usage: build_docs.sh [serve]
	exit 1
}

# Do a few sanity checks...

hash git >> /dev/null 2>&1 || {
    echo "Oh dear. I require Git, but it's not installed."
    exit 1
}

hash jekyll >> /dev/null 2>&1 || {
    echo "Oh dear. It looks like jekyll isn't installed."
    exit 1
}

# Move to the root directory...

GIT_DIR=`git rev-parse --show-toplevel`

if [[ $PWD != $GIT_DIR ]]; then
    echo "Changing to the Git root directory..."
    cd $GIT_DIR
fi

if [[ $# -eq 1 && $1 == "serve" ]]; then
    jekyll serve --source $DOCS_DIR --destination $SITE_DIR
    exit 0
elif [[ $# -eq 1 && $1 != "serve" ]]; then
    usage
fi

# Build documentation
jekyll build --source $DOCS_DIR --destination $SITE_DIR --plugins $PLUGINS_DIR --layouts $LAYOUTS_DIR

git checkout $DOC_BRANCH || {
    echo "Failed to checkout $DOC_BRANCH"
    exit 1
}
