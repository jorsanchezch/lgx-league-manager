/** @type {import('next').NextConfig} */
const path = require('path')

const nextConfig = {
  reactStrictMode: true,
  sassOptions: {
    includePaths: [path.join(__dirname, 'src/styles')],
    additionalData: `@import "variables.scss";`,
  },
  typescript: {}
}

module.exports = nextConfig
