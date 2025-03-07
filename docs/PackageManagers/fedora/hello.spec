Name:		hello
Version:	0.0.1
Release:    1%{?dist}
Summary:	hello world rpm package

License:	MIT
URL:		https://fedoraproject.org
SOURCE0:	%{name}-%{version}.tar.gz
BuildArch:	x86_64

BuildRequires:	gcc
Requires:	gcc

%description
My first rpm package

%global debug_package %{nil}

%prep
%setup -q


%build
gcc -o hello hello.c


%install
mkdir -p %{buildroot}/%{_bindir}
cp -p hello %{buildroot}/%{_bindir}/


%files
%{_bindir}/%{name}


%changelog
* Sat May 27 2023 FirstName Surname <fedora@fedora.com> - 0.0.1
- Initial Package


%pre
echo "Before Install"

%post
echo "After Install"

%preun
echo "Before Remove"

%postun
echo "After Remove"
