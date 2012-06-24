Summary:	BIEW is Binary vIEWer and editor
Summary(pl):	BIEW jest przegl�dark� plik�w binarnych z edytorem
Summary(ru):	biew - �������� �������� ������ � ��������������
Summary(uk):	biew - �������� �צ������ ���̦� � �������������
Name:		biew
Version:	532
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/biew/%{name}-%{version}.tar.bz2
#Patch0:		%{name}-CURSES.patch
URL:		http://biew.sourceforge.net/
BuildRequires:	ncurses-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BIEW is advanced Binary vIEWer with built-in editor for binary,
hexadecimal and disassembler modes. His disassembler supports many
processors (Pentium4, K7 Athlon, Cyrix-M2) and many file formats
(MZ, NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF, a.out, coff32 PharLap,
rdoff).

%description -l pl
BIEW (Binary vIEWer) jest zaawansowan� przegl�dark� i edytorem plik�w
binarnych. Zawiera wbudowany disasembler ze wsparciem dla wielu nowych
procesor�w (w tym Pentium4, Athlon i Cyrix-M2) oraz wielu format�w
plik�w wykonywalnych (MZ, NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF,
a.out, coff32 PharLap, rdoff).

%description -l ru
biew - ��� �����������/�������� �������� ������ � ������������ ���������
� �������������� � ��������, ����������������� � �������������� �������.
�������������� ��������� ������������ ������ PentiumIV/K7-Athlon/Cyrix-M2,
���� ��������� ������������� ���������, ������ �������� �������� MZ, NE, PE,
LE, LX, DOS.SYS, NLM, ELF.

%description -l uk
biew - �� ����������/�������� �צ������ ���̦� � �����צ��� ��������� ��
����������� � �צ�������, ۦ�������������� �� ��������������� �������.
������դ���� ��Ħ����� ���������� ������ PentiumIV/K7-Athlon/Cyrix-M2,
� ��������� ����̦���� ��������, ������ �������� �����Ԧ� MZ, NE, PE, LE,
LX, DOS.SYS, NLM, ELF.

%prep
%setup -q
#%patch0 -p1

%build
%ifarch %{ix86}
 target=%{_target_cpu}
%else
 target=generic
%endif

%{__make} \
	TARGET_PLATFORM=$target \
	TARGET_OS=unix \
	INCS="-I. -I/usr/include/ncurses" \
	compilation=%{?debug:debug}%{!?debug:advance}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}/ $RPM_BUILD_ROOT%{_libdir}/biew/

install biew $RPM_BUILD_ROOT%{_bindir}
install bin_rc/{biew.hlp,skn/*} $RPM_BUILD_ROOT%{_libdir}/biew/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*txt doc/*.en
%lang(ru) %doc doc/*.ru
%attr(755,root,root) %{_bindir}/biew
%{_libdir}/biew
