from argparse import ArgumentParser


def parse_args():
    parser=ArgumentParser()
    parser.add_argument('--video_path',
                        default='sequences/')
    parser.add_argument('--target_video',
                        default=['Couple'])

    # Default parameters used in the ICCV 2015 paper
    parser.add_argument('--dim_feature', default=31,
                        help="HOG feature parameters")
    parser.add_argument('--colorspace', default='gray',
                        help="Grayscale feature parameters")
    parser.add_argument('--n_dim', default=1)

    # Global feature parameters
    # t_features={
    #     ...struct('getFeature',@get_colorspace, 'fparams',grayscale_params),...  # Grayscale is not used as default
    #     struct('getFeature',@get_fhog,'fparams',hog_params),...
    # }
    parser.add_argument('--cell_size', default=4,
                        help='Feature cell size')
    parser.add_argument('--cell_selection_thresh', default=0.75**2,
                        help='Threshold for reducing the cell size in low-resolution cases')

    # Filter parameters
    parser.add_argument('--search_area_shape', default='square',
                        help="The shape of the training/detection window: 'proportional', 'square' or 'fix_padding'")
    parser.add_argument('--search_area_scale', default=4.0,
                        help="the size of the training/detection area proportional to the target size")
    parser.add_argument('--filter_max_area', default=50**2,
                        help="the size of the training/detection area in feature grid cells")

    # Learning parameters
    parser.add_argument('--learning_rate', default=0.025,
                        help="learning rate")
    parser.add_argument('--output_sigma_factor', default=1/16,
                        help="standard deviation of the desired correlation output (proportional to target)")
    parser.add_argument('--init_strategy', default='indep',
                        help="strategy for initializing the filter: 'const_reg' or 'indep'")
    parser.add_argument('--num_GS_iter', default=4,
                        help="number of Gauss-Seidel iterations in the learning")

    # Detection parameters
    parser.add_argument('--refinement_iterations', default=1,
                        help="number of iterations used to refine the resulting position in a frame")
    parser.add_argument('--interpolate_response', default=4,
                        help="correlation score interpolation strategy: 0 - off, 1 - feature grid, 2 - pixel grid, 4 - Newton's method")
    parser.add_argument('--newton_iterations', default=5,
                        help="number of Newton's iteration to maximize the detection scores")

    # Regularization window parameters
    parser.add_argument('--use_reg_window', default=1,
                        help="wather to use windowed regularization or not")
    parser.add_argument('--reg_window_min', default=0.1,
                        help="the minimum value of the regularization window")
    parser.add_argument('--reg_window_edge', default=3.0,
                        help="the impact of the spatial regularization (value at the target border), depends on the detection size and the feature dimensionality")
    parser.add_argument('--reg_window_power', default=2,
                        help="the degree of the polynomial to use (e.g. 2 is a quadratic window)")
    parser.add_argument('--reg_sparsity_threshold', default=0.05,
                        help="a relative threshold of which DFT coefficients that should be set to zero")
    parser.add_argument('--reg_lambda', default=0.01,
                        help="the weight of the standard (uniform) regularization, only used when use_reg_window == 0")

    # Scale parameters
    parser.add_argument('--number_of_scales', default=7)
    parser.add_argument('--scale_step', default=1.01)

    # Debug and visualization
    parser.add_argument('--visualization', default=1)
    parser.add_argument('--debug', default=0)

    params = parser.parse_args()
    return params