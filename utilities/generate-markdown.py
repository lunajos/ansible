#!/usr/bin/python3

# Import tools to list dirs
import os

# Directory containing Ansible scripts
ansibleDir = "/home/admin/develop/ansible-docugen/example/scripts"
# Directory to put markdown documensts
mdDir = "/home/admin/develop/ansible-docugen/example/docs/"
# New Markdwon file
mdFile = ""

markdownLine = []
# List of styles - h1, h2, h3, h4, comment, code
def writeMdLine(mdFile, tag):

    if tag["style"] == "hosts":
        markdownLine.append("## hosts\n")
        markdownLine.append("- " + tag["content"] + "\n\n")
        markdownLine.append("----\n\n")
    if tag["style"] == "title":
        markdownLine.append("# " + tag["content"] + "\n\n")
    if tag["style"] == "name":
        markdownLine.append("` `  \n")
        markdownLine.append("` `  \n")
        markdownLine.append("## " + tag["content"] + "\n\n")
    if tag["style"] == "comment":
        markdownLine.append("*" + tag["content"] + "*" + "\n\n") 
    if tag["style"] == "code":
        markdownLine.append("```\n")
        markdownLine.append(tag["content"])
        markdownLine.append("\n```\n\n")
    if tag["style"] == "input":
        markdownLine.append("### input\n")
        markdownLine.append("```\n")
        markdownLine.append(tag["content"])
        markdownLine.append("\n```\n\n")
    if tag["style"] == "output":
        markdownLine.append("### output\n")
        markdownLine.append("```\n")
        markdownLine.append(tag["content"])
        markdownLine.append("\n```\n\n")

    # Write to file
    with open(mdFile, "w") as file:
        file.writelines(markdownLine)

    # Rename from yml to md
    base = os.path.splitext(mdFile)[0]
    os.rename(mdFile, base + ".md")        


# Tag may start be - # @name,  # @comment,  # @code,  # @input,  # @output, 
def getTag(ansibleScriptPath, markdownPath):
    with open(ansibleScriptPath, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        content=""
        tagline=""
        if line.strip().startswith("# @hosts"):
            content=line.strip()[9:].strip()
            tagline={"style": "hosts", "content" : content }
            writeMdLine(markdownPath, tagline) 
        if line.strip().startswith("# @title"):
            content=line.strip()[9:].strip()
            tagline={"style": "title", "content" : content }
            writeMdLine(markdownPath, tagline) 
        if line.strip().startswith("# @name"):
            content=line.strip()[8:].strip()
            tagline={"style": "name", "content" : content }
            writeMdLine(markdownPath, tagline) 
        if line.strip().startswith("# @comment"):
            content=line.strip()[11:].strip()
            tagline={"style": "comment", "content" : content }
            writeMdLine(markdownPath, tagline) 
        if line.strip().startswith("# @code"):
            content=line.strip()[8:].strip()
            tagline={"style": "code", "content" : content }
            writeMdLine(markdownPath, tagline) 
        if line.strip().startswith("# @input"):
            content=line.strip()[9:].strip()
            tagline={"style": "input", "content" : content }
            writeMdLine(markdownPath, tagline) 
        if line.strip().startswith("# @output"):
            content=line.strip()[10:].strip()
            tagline={"style": "output", "content" : content }
            writeMdLine(markdownPath, tagline) 

# Loop through each file in the directory
for filename in os.listdir(ansibleDir):
    # Check for ansible scripts. Assume they end with yml or yaml
    if filename.endswith(".yml") or filename.endswith(".yaml"): 
        
        # Generate full path to new markdown file 
        mdFilePath = os.path.join(mdDir, filename)
        ansibleFilePath = os.path.join(ansibleDir, filename)
        markdownLine = []

        getTag(ansibleFilePath, mdFilePath)

