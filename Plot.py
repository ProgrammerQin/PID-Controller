def noise():  # noise removal function
    if load_img:  # Check if the image is loaded
        try:
            img = read_img  # Read the return image veriable
            fig = plt.figure()  # Plot figure
            if (len(img.shape) < 3):  # Check if image is Gray
                dst = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)  # Noise removal function for gray image
                # Plot orignal and noise removal images side by side
                plt.subplot(121), plt.imshow(img, 'gray'), plt.title("Image Noise Removal Processing\n\nOrignal")
                plt.subplot(122), plt.imshow(dst, 'gray'), plt.title("Noise_Removal")
                plt.show()  # Show plot function
                fig.savefig('out_5.jpg', dpi=200)  # Save the image into JPG format


# 8. Visualize Predicted Price
data = stock_data.filter(['Close'])
train = data[:training_data_len]
validation = data[training_data_len:]
validation['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.plot(train)
plt.plot(validation[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()
