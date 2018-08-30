import { dogs } from '../../constants/mock/images';

export const search = image => {
  return new Promise(resolve => {
    fetch('http://localhost:5000/images', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        base64: image,
      })
    })
    .then(response => response.json())
    .then((data) => {
      resolve(data);
    });
  });
};
