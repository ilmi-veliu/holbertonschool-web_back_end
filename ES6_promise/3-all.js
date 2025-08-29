import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const userInfo = results[1];
      const photoInfo = results[0];
      console.log(photoInfo.body, userInfo.firstName, userInfo.lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
