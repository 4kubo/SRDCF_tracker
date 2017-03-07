import csv
from pandas import read_csv

def load_video_info(video_path):
    with open(video_path+'/groundtruth_rect.txt') as f:
        reader = csv.reader(f)
        for row in reader:
            print row

    # seq.len = size(ground_truth, 1);
    # seq.init_rect = ground_truth(1,:);
    #
    # img_path = [video_path '/img/'];
    #
    # if exist([img_path num2str(1, '%04i.png')], 'file'),
    #     img_files = num2str((1:seq.len)', [img_path '%04i.png']);
    # elseif exist([img_path num2str(1, '%04i.jpg')], 'file'),
    #     img_files = num2str((1:seq.len)', [img_path '%04i.jpg']);
    # elseif exist([img_path num2str(1, '%04i.bmp')], 'file'),
    #     img_files = num2str((1:seq.len)', [img_path '%04i.bmp']);
    # else
    #     error('No image files to load.')
    # end
    #
    # seq.s_frames = cellstr(img_files);
    #
    # end
     # [h, w]
    wsize = [seq.init_rect(1,4), seq.init_rect(1,3)]
    init_pos = [seq.init_rect(1,2), seq.init_rect(1,1)] + floor(wsize/2)
    s_frames = seq.s_frames