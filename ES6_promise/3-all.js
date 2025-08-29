import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const userInfo = results[1]; // ← aussi corrigé la casse
      console.log(userInfo.firstName, userInfo.lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
