Name:           perl-Test-SubCalls
Version:        1.09
Release:        1%{?dist}
Summary:        Track the number of times subs are called

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-SubCalls/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Test-SubCalls-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Hook::LexWrap) >= 0.20
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::More) >= 0.60
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# for improved tests
BuildRequires:  perl(Test::CPAN::Meta) >= 0.12
# FIXME: Fedora's Pod::Simple is outdated
# BuildRequires:  perl(Pod::Simple) >= 3.07
BuildRequires:  perl(Pod::Simple)
BuildRequires:	perl(Test::Pod) >= 1.26
BuildRequires:  perl(Test::MinimumVersion) >= 0.008

%description
There are a number of different situations (like testing cacheing
code) where you want to want to do a number of tests, and then verify
that some underlying subroutine deep within the code was called a
specific number of times.


%prep
%setup -q -n Test-SubCalls-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test AUTOMATED_TESTING=1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Wed Oct  7 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.09-1
- update to new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 05 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.08-1
- Upstream update.
- Activate AUTOMATED_TESTING.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-3
- Rebuild for perl 5.10 (again)

* Sat Jan 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-1
- bump to 1.07
- license fix

* Fri May 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-1
- Update to 1.06.

* Tue Apr 25 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-1
- First build.
