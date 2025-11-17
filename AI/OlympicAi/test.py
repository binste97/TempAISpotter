if __name__ == "__main__":


    from AI.MediaPipe import MediaPipeVideoProcessor
    
    try:
        import traceback
        # Paths to input and output video files
<<<<<<< HEAD
        input_video = "videos/snatch_video.mp4"      # Replace with your actual test video path
        output_video = "snatch_processed_res.mp4"    # This will be created with skeleton overlay
=======
        input_video = "videos/new_backside.mp4"      # Replace with your actual test video path
        output_video = "squat_back_res.mp4"    # This will be created with skeleton overlay
>>>>>>> feature/frontend-upload-analysis

        # Create processor and run
        processor = MediaPipeVideoProcessor()
        processor.process_video(input_video, output_video, all_landmarks=False, calculate_angle=True)

        print("Processing complete. Check:", output_video)

    except Exception as e:
        print("An error occurred during processing:")
        print(e)
        traceback.print_exc()