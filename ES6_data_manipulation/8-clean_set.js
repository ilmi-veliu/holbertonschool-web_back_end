export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const stokage = [];
  for (const element of set) {
    if (element.startsWith(startString)) {
      stokage.push(element.slice(startString.length));
    }
  }
  return stokage.join('-');
}
