%{?_javapackages_macros:%_javapackages_macros}

Name:           gpars
Version:        1.2.1
Release:        8%{?dist}
Summary:        Groovy Parallel Systems
License:        ASL 2.0 and Public Domain
URL:            http://gpars.codehaus.org
BuildArch:      noarch

# ./generate-tarball.sh %{version}
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        generate-tarball.sh
#Source100:      http://central.maven.org/maven2/org/codehaus/gpars/%{name}/%{version}/%{name}-%{version}.pom

Patch0:         0001-JSR-166.patch
Patch1:         0002-Enable-XMvn-local-mode.patch
Patch2:         0001-Port-build-script-to-current-gradle.patch
Patch3:         gpars-1.2.1-port-to-netty-3.10.6.patch
Patch100:       gpars-1.2.1-gradle-use-maven-plugin.patch
Patch101:       gpars-1.2.1-gradle-use-local-repository.patch
BuildRequires:  gradle-local >= 2.1-0.10
BuildRequires:  maven-local
BuildRequires:  apache-parent
BuildRequires:  extra166y
BuildRequires:  jcsp
BuildRequires:  netty3
BuildRequires:  groovy-lib
BuildRequires:  multiverse

%description
The GPars framework offers Java developers intuitive and safe ways to
handle Java or Groovy tasks concurrently. Leveraging the enormous
flexibility of the Groovy programming language and building on proven
Java technologies, we aim to make concurrent programming for
multi-core hardware intuitive, robust and enjoyable.

GPars is a multi-paradigm concurrency framework, offering several
mutually cooperating high-level concurrency abstractions, such as
Dataflow operators, Promises, CSP, Actors, Asynchronous Functions,
Agents and Parallel Collections.

%prep
%setup -q
cp %{SOURCE1} .
rm -rf lib/ gradle/wrapper/
rm -rf src/main/groovy/groovyx/gpars/extra166y/
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch100 -p1
%patch101 -p1

%build
#% gradle_build -f
gradle build -x test -x buildGuide -Dfile.encoding=UTF-8 --offline -s

%install
%mvn_artifact buils/poms/pom-default.xml build/libs/%{name}-%{version}.jar
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE-2.0.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://	fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 gil cattaneo <puntogil@libero.it> 1.2.1-7
- build fix for netty 3.10.6.Final

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-5
- Build with %%gradle_build

* Tue Jun 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-4
- Use gradle-local script for building

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 1.2.1-3
- Port build script to current gradle

* Mon Feb  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-2
- Use generic netty3 compat version
- Resolves: rhbz#1187710

* Wed Nov 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-1
- Non-bootstrap build

* Wed Nov 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.8
- Bootstrap build using prebuilt binaries

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.7
- Include generate-tarball.sh as a source

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.6
- Remove gradle-wrapper bundled JAR
- Fix spelling error
- Fix ownership of created directories
- Unbuldle extra166y
- Remove non-free content from source tarball

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.5
- Add BR on apache-parent

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.4
- Use XMvn resolver factory method

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.3
- Install Apache License text

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.2
- Install generated POM instead of prebuilt one

* Tue Nov  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-0.1
- Initial packaging
