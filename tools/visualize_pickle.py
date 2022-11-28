import pickle
from tools.visual_utils.open3d_vis_utils import draw_scenes
if __name__ == '__main__':
    with open('demo_result.pkl','rb') as f:
        data_dict=pickle.load(f)
    pred=data_dict['result']
    print(data_dict)
    draw_scenes(
        points=data_dict['points'][:, 1:], ref_boxes=pred['pred_boxes'],
        ref_scores=pred[0]['pred_scores'], ref_labels=pred[0]['pred_labels']
    )