import cv2

def draw_boxes(frame, detections, fps=None):
    """
    detections: list of (xmin, ymin, xmax, ymax, id, cls_name, conf)
    """
    for (x1, y1, x2, y2, track_id, cls_name, conf) in detections:
        color = (0, 255, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        label = f"{cls_name} {track_id} {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    if fps is not None:
        cv2.putText(frame, f"FPS: {fps:.2f}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame