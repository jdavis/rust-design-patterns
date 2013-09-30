#!/bin/sh

# Set our variables
DOC_BRANCH="gh-pages"
SITE_DIR="_site/"

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

git checkout $DOC_BRANCH || {
    echo "Failed to checkout $DOC_BRANCH"
    exit 1
}
