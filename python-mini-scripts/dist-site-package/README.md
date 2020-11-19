# Dist Package and Site Package

`dist-packages` is the debian-specific directory where apt and friends install their stuff, and 

`site-packages` is the standard pip directory.

The problem is -- what happens when different versions of the same package are present in different directories?

My solution to the problem is to make dist-packages a symlink to site-packages:

```sh
for d in $(find $WORKON_HOME -type d -name dist-packages); do
  pushd $d
  cd ..
  if test -d dist-packages/__pycache__; then
    mv -v dist-packages/__pycache__/* site-packages/__pycache__/
    rmdir -v dist-packages/__pycache__
  fi
  mv -v dist-packages/* site-packages/
  rmdir -v dist-packages
  ln -sv site-packages dist-packages
  popd
done
```

(if you are not using gnu tools, remove the -v option).