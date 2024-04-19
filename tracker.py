import math

class Tracker:
    def __init__(self):
        # Store the center positions and frame count of the objects
        self.center_points = {}
        # Keep the count of the IDs
        self.id_count = 0
        # Maximum allowed frames for an object to be considered as lost
        self.max_lost = 5

    def update(self, objects_rect):
        # Objects boxes and ids
        objects_bbs_ids = []
        # Temporary dictionary to store updated center points
        new_center_points = {}

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = x + w // 2
            cy = y + h // 2

            # Find out if that object was detected already
            same_object_detected = False
            for id, (pt, lost_frames) in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 35:
                    new_center_points[id] = ((cx, cy), 0)  # Reset lost_frames since the object is detected
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if not same_object_detected:
                new_center_points[self.id_count] = ((cx, cy), 0)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # Update center_points, increase lost_frames for each undetected object
        updated_center_points = {}
        for id, (pt, lost_frames) in self.center_points.items():
            if id in new_center_points:
                updated_center_points[id] = new_center_points[id]
            else:
                if lost_frames < self.max_lost:
                    updated_center_points[id] = (pt, lost_frames + 1)  # Increment the frame count
                    objects_bbs_ids.append([pt[0] - w // 2, pt[1] - h // 2, w, h, id])  # Optional: include last known position

        # Replace the old center points with the updated ones
        self.center_points = updated_center_points
        return objects_bbs_ids
