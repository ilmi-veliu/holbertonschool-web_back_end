module.exports = {
    env: {
      node: true,
      es6: true,
      jest: true,
    },
    extends: ['airbnb-base', 'plugin:jest/recommended'],
    plugins: ['import', 'jest'],
    parserOptions: {
      ecmaVersion: 2020,
      sourceType: 'module',
    },
    settings: {
      'import/resolver': {
        node: { extensions: ['.js'] },
      },
    },
    rules: {
      'no-console': 'off',
      'prefer-const': 'error',
      'eol-last': ['error', 'always'],
    },
    overrides: [
      {
        files: ['**/*-main.js'],
        rules: {
          'import/extensions': 'off', // <- autorise ./fichier.js dans les mains
        },
      },
    ],
  };