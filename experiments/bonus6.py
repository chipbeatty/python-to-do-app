
contents = ["All carrots are to be sllicesd longituinally.",
            "The carrots were repostedly sliced.",
            "Carrots are orange"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)