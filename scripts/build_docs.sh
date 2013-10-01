#!/bin/sh

# Set our variables
DOC_BRANCH="gh-pages"
DOCS_DIR="docs/"
SITE_DIR="_site/"
PLUGINS_DIR="$DOCS_DIR/_plugins/"
LAYOUTS_DIR="$DOCS_DIR/_layouts/"

#
# Documentation functions
#

# Prints the basic usage of build_docs.sh.
function usage() {
    echo Usage: build_docs.sh [serve]
}

# Uses Jekyll to serve up the documentation.
function serve() {
    echo Serving up documentation...
    echo

    jekyll serve --source $DOCS_DIR --destination $SITE_DIR
}

# Checkouts the gh-pages branch, commits the generated documentation and then
# pushes it.
function deploy() {
    echo Deploying documentation...
    echo

    git checkout $DOC_BRANCH || {
        echo "Failed to checkout $DOC_BRANCH"
        exit 1
    }

    mv $SITE_DIR/* ./

    git add .
    git commit -m "AUTO: Update generated documentation"
    git push origin $DOC_BRANCH

    echo
    echo Deploy finished.
}

# The default function, it just builds the documentation using Jekyll.
function build() {
    echo Building documentation...
    echo

    # Build documentation
    echo jekyll build --source $DOCS_DIR --destination $SITE_DIR --plugins $PLUGINS_DIR --layouts $LAYOUTS_DIR
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

if [[ $# -eq 0 ]]; then
    build
else
    # Run functions for the arguments given
    for cmd in "$@"
    do
        case "$cmd" in
            "build")
                build;;
            "deploy")
                deploy;;
            "serve")
                serve;;
            *)
                usage;;
        esac
    done
fi
