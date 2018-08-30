export const encodeToBase64 = (file, onSuccess, onError) => {
  const rd = new FileReader();
  rd.readAsDataURL(file);

  rd.onload = () => {
    onSuccess(rd.result);
  };

  rd.onerror = error => {
    onError(error);
  };
};
