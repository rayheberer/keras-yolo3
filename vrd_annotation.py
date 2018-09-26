import json


image_directory = "model_data/sg_dataset/sg_train_images/"


def format_boxes(objects):
    boxes = set()
    for relation in objects:
        for obj_type in ["subject", "object"]:
            obj = relation[obj_type]
            bbox_yyxx = obj["bbox"]
            category = obj["category"]

            bbox_xyxy = [str(bbox_yyxx[i]) for i in [2, 0, 3, 1]]

            box = ",".join(bbox_xyxy + [str(category)])
            boxes.add(box)

    return " ".join(list(boxes))


def format_annotations(annotations):
    rows = []

    for filename, objects in annotations.items():
        image_file_path = image_directory + filename
        boxes = format_boxes(objects)
        rows.append(image_file_path + " " + boxes)

    return "\n".join(rows)


def main():
    with open("model_data/sg_dataset/annotations_train.json") as file:
        annotations = json.load(file)

    formatted_annotations = format_annotations(annotations)

    f = open("model_data/vrd_annotations.txt", "w")
    f.write(formatted_annotations)
    f.close()


if __name__ == '__main__':
    main()
