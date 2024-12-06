import os
import csv
import torch
from PIL import Image
from ImageMatcher import load_models, extract_features, find_most_similar_image, load_dataset_features

# Folder paths for images and features
IMAGE_FOLDER = r"images"  # Update to your folder path
QUERY_IMAGE_PATH = r"evaluation\image-matching\query\listing_1_image_1.png_20240927_122438.png"  # Path to the query image
OUTPUT_FOLDER = r"output"  # Output folder for the CSV files

SIMCLR_FEATURES_FILE = 'simclr_features.pkl'
DEIT_FEATURES_FILE = 'deit_features.pkl'
CLIP_FEATURES_FILE = 'clip_features.pkl'
CNN_FEATURES_FILE = 'cnn_features.pkl'

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def save_to_csv(filename, query_image, similar_images, similarity_scores):
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Query Image", "Similar Images", "Similarity Scores"])
        writer.writerow([
            query_image,
            ", ".join(similar_images),
            ", ".join(similarity_scores)
        ])
    print(f"Results saved to {filepath}")

def main():
    # Load models
    simclr_model, deit_model, clip_model, cnn_model = load_models()

    # Load query image
    query_image = Image.open(QUERY_IMAGE_PATH).convert("RGB")

    # Extract features for the query image
    query_features_cnn = extract_features(cnn_model, query_image, 'base_cnn')
    query_features_clip = extract_features(clip_model, query_image, 'clip')
    query_features_deit = extract_features(deit_model, query_image, 'deit')

    # Load precomputed dataset features
    dataset_features_cnn = load_dataset_features(IMAGE_FOLDER, cnn_model, 'base_cnn', CNN_FEATURES_FILE)
    dataset_features_clip = load_dataset_features(IMAGE_FOLDER, clip_model, 'clip', CLIP_FEATURES_FILE)
    dataset_features_deit = load_dataset_features(IMAGE_FOLDER, deit_model, 'deit', DEIT_FEATURES_FILE)

    # Find similar images for each model
    similar_images_cnn = find_most_similar_image(query_features_cnn, dataset_features_cnn)
    similar_images_clip = find_most_similar_image(query_features_clip, dataset_features_clip)
    similar_images_deit = find_most_similar_image(query_features_deit, dataset_features_deit)

    # Combine CLIP and DEIT results
    combined_clip_deit = similar_images_clip + similar_images_deit
    combined_clip_deit = sorted(combined_clip_deit, key=lambda x: x[1], reverse=True)[:5]

    # Prepare data for CSVs
    def prepare_csv_data(results):
        similar_images = [img for img, _ in results]
        similarity_scores = [f"{score:.4f}" for _, score in results]
        return similar_images, similarity_scores

    similar_images_cnn_paths, similarity_scores_cnn = prepare_csv_data(similar_images_cnn[:5])
    similar_images_clip_paths, similarity_scores_clip = prepare_csv_data(similar_images_clip[:5])
    similar_images_deit_paths, similarity_scores_deit = prepare_csv_data(similar_images_deit[:5])
    combined_clip_deit_paths, combined_clip_deit_scores = prepare_csv_data(combined_clip_deit)

    # Save results to separate CSV files
    save_to_csv("cnn_results.csv", QUERY_IMAGE_PATH, similar_images_cnn_paths, similarity_scores_cnn)
    save_to_csv("clip_results.csv", QUERY_IMAGE_PATH, similar_images_clip_paths, similarity_scores_clip)
    save_to_csv("deit_results.csv", QUERY_IMAGE_PATH, similar_images_deit_paths, similarity_scores_deit)
    save_to_csv("clip_deit_combined_results.csv", QUERY_IMAGE_PATH, combined_clip_deit_paths, combined_clip_deit_scores)

if __name__ == "__main__":
    main()
