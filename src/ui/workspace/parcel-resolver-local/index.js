const fs = require('fs'),
    path = require('path'),
    { Resolver } = require('@parcel/plugin')

//https://parceljs.org/plugin-system/resolver/#ResolveResult

const pkgJson = require(path.join(process.cwd(), './package.json')),
    targetDir = path.join(process.cwd(), pkgJson.targets.default.distDir),
    copyRules = pkgJson.parcelLocal.copy

if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir)

module.exports = new Resolver({
    async resolve({ specifier }) {
        if (!Array.isArray(copyRules)) return null;
        const rule = copyRules.find(x => specifier === x.name)
        if (!rule) return null;


        const from = path.join(process.cwd(), rule.target),
            to = path.join(targetDir, path.basename(from));

        if (!fs.existsSync(to)) fs.copyFileSync(from, to);
        console.log(`Copied file to ${specifier}`)

        return {
            isExcluded: true
        }
    }
});