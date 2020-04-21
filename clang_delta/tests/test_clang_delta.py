import os
import unittest
import subprocess

class TestClangDelta(unittest.TestCase):

    @classmethod
    def check_clang_delta(cls, testcase, arguments):
        current = os.path.dirname(__file__)
        binary = os.path.join(current, '../clang_delta')
        cmd = '%s %s %s' % (binary, os.path.join(current, testcase), arguments)
        output = subprocess.check_output(cmd, shell=True, encoding='utf8')
        expected = open(os.path.join(current, os.path.splitext(testcase)[0] + '.output')).read()
        assert output == expected

    @classmethod
    def check_query_instances(cls, testcase, arguments, expected):
        current = os.path.dirname(__file__)
        binary = os.path.join(current, '../clang_delta')
        cmd = '%s %s %s' % (binary, os.path.join(current, testcase), arguments)
        output = subprocess.check_output(cmd, shell=True, encoding='utf8')
        assert output.strip() == expected

    def test_aggregate_to_scalar_cast(self):
        self.check_clang_delta('aggregate-to-scalar/cast.c', '--transformation=aggregate-to-scalar --counter=1')

    def test_aggregate_to_scalar_test1(self):
        self.check_clang_delta('aggregate-to-scalar/test1.c', '--transformation=aggregate-to-scalar --counter=1')

    def test_aggregate_to_scalar_test1(self):
        self.check_clang_delta('aggregate-to-scalar/test1.cc', '--transformation=aggregate-to-scalar --counter=1')

    def test_aggregate_to_scalar_test2(self):
        self.check_clang_delta('aggregate-to-scalar/test2.c', '--transformation=aggregate-to-scalar --counter=1')

    def test_aggregate_to_scalar_test2(self):
        self.check_clang_delta('aggregate-to-scalar/test2.cc', '--transformation=aggregate-to-scalar --counter=1')

    def test_aggregate_to_scalar_test3(self):
        self.check_clang_delta('aggregate-to-scalar/test3.c', '--transformation=aggregate-to-scalar --counter=1')

    def test_aggregate_to_scalar_test4(self):
        self.check_clang_delta('aggregate-to-scalar/test4.c', '--transformation=aggregate-to-scalar --counter=1')

    def test_callexpr_to_value_macro1(self):
        self.check_clang_delta('callexpr-to-value/macro1.c', '--transformation=callexpr-to-value --counter=1')

    def test_callexpr_to_value_macro2(self):
        self.check_clang_delta('callexpr-to-value/macro2.c', '--transformation=callexpr-to-value --counter=1')

    def test_callexpr_to_value_test1(self):
        self.check_clang_delta('callexpr-to-value/test1.c', '--transformation=callexpr-to-value --counter=1')

    def test_callexpr_to_value_test2(self):
        self.check_clang_delta('callexpr-to-value/test2.c', '--transformation=callexpr-to-value --counter=1')

    def test_copy_propagation_copy1(self):
        self.check_clang_delta('copy-propagation/copy1.cpp', '--transformation=copy-propagation --counter=1')

    def test_copy_propagation_copy2(self):
        self.check_clang_delta('copy-propagation/copy2.cpp', '--transformation=copy-propagation --counter=2')

    def test_empty_struct_to_int_empty_struct(self):
        self.check_clang_delta('empty-struct-to-int/empty-struct.cpp', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_empty_struct2(self):
        self.check_clang_delta('empty-struct-to-int/empty-struct2.cpp', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_empty_struct3(self):
        self.check_clang_delta('empty-struct-to-int/empty-struct3.cpp', '--transformation=empty-struct-to-int --counter=2')

    def test_empty_struct_to_int_empty_struct4(self):
        self.check_clang_delta('empty-struct-to-int/empty-struct4.cpp', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_empty_struct5(self):
        self.check_clang_delta('empty-struct-to-int/empty-struct5.cpp', '--transformation=empty-struct-to-int --counter=1')

    @unittest.skip(reason='Libclang segfault')
    def test_empty_struct_to_int_empty_struct6(self):
        self.check_clang_delta('empty-struct-to-int/empty-struct6.c', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_empty_struct7(self):
        self.check_clang_delta('empty-struct-to-int/empty-struct7.c', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_struct_int(self):
        self.check_clang_delta('empty-struct-to-int/struct_int.c', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_test1(self):
        self.check_clang_delta('empty-struct-to-int/test1.cc', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_test2(self):
        self.check_clang_delta('empty-struct-to-int/test2.cc', '--transformation=empty-struct-to-int --counter=1')

    def test_empty_struct_to_int_test3(self):
        self.check_clang_delta('empty-struct-to-int/test3.c', '--transformation=empty-struct-to-int --counter=1')

    def test_local_to_global_macro(self):
        self.check_clang_delta('local-to-global/macro.c', '--transformation=local-to-global --counter=1')

    def test_local_to_global_unnamed_1(self):
        self.check_clang_delta('local-to-global/unnamed_1.c', '--transformation=local-to-global --counter=1')

    def test_local_to_global_unnamed_2(self):
        self.check_clang_delta('local-to-global/unnamed_2.c', '--transformation=local-to-global --counter=1')

    def test_local_to_global_unnamed_3(self):
        self.check_clang_delta('local-to-global/unnamed_3.c', '--transformation=local-to-global --counter=2')

    def test_param_to_global_macro(self):
        self.check_clang_delta('param-to-global/macro.c', '--transformation=param-to-global --counter=1')

    def test_reduce_array_dim_non_type_temp_arg(self):
        self.check_clang_delta('reduce-array-dim/non-type-temp-arg.cpp', '--transformation=reduce-array-dim --counter=1')

    def test_reduce_pointer_level_scalar_init_expr(self):
        self.check_clang_delta('reduce-pointer-level/scalar-init-expr.cpp', '--transformation=reduce-pointer-level --counter=1')

    def test_remove_enum_member_value_builtin_macro(self):
        self.check_clang_delta('remove-enum-member-value/builtin_macro.c', '--transformation=remove-enum-member-value --counter=1')

    def test_remove_nested_function_remove_nested_func1(self):
        self.check_clang_delta('remove-nested-function/remove_nested_func1.cc', '--transformation=remove-nested-function --counter=1')

    def test_remove_unused_field_designated1(self):
        self.check_clang_delta('remove-unused-field/designated1.c', '--transformation=remove-unused-field --counter=1')

    def test_remove_unused_field_designated2(self):
        self.check_clang_delta('remove-unused-field/designated2.c', '--transformation=remove-unused-field --counter=2')

    def test_remove_unused_field_designated3(self):
        self.check_clang_delta('remove-unused-field/designated3.c', '--transformation=remove-unused-field --counter=3')

    def test_remove_unused_field_designated4(self):
        self.check_clang_delta('remove-unused-field/designated4.c', '--transformation=remove-unused-field --counter=1')

    def test_remove_unused_field_designated5(self):
        self.check_clang_delta('remove-unused-field/designated5.c', '--transformation=remove-unused-field --counter=2')

    def test_remove_unused_field_unused_field1(self):
        self.check_clang_delta('remove-unused-field/unused_field1.c', '--transformation=remove-unused-field --counter=1')

    def test_remove_unused_field_unused_field2(self):
        self.check_clang_delta('remove-unused-field/unused_field2.c', '--transformation=remove-unused-field --counter=2')

    def test_remove_unused_field_unused_field3(self):
        self.check_clang_delta('remove-unused-field/unused_field3.cpp', '--transformation=remove-unused-field --counter=1')

    def test_remove_unused_function_class(self):
        self.check_clang_delta('remove-unused-function/class.cc', '--transformation=remove-unused-function --counter=1')

    def test_remove_unused_function_inline_ns(self):
        self.check_query_instances('remove-unused-function/inline_ns.cc', '--query-instances=remove-unused-function',
                'Available transformation instances: 0')

    def test_remove_unused_function_macro1(self):
        self.check_clang_delta('remove-unused-function/macro1.cc', '--transformation=remove-unused-function --counter=1')

    def test_remove_unused_function_macro2(self):
        self.check_clang_delta('remove-unused-function/macro2.cc', '--transformation=remove-unused-function --counter=1')

    def test_remove_unused_function_macro3(self):
        self.check_clang_delta('remove-unused-function/macro3.cc', '--transformation=remove-unused-function --counter=1')

    def test_remove_unused_function_template1(self):
        self.check_clang_delta('remove-unused-function/template1.cc', '--transformation=remove-unused-function --counter=1')

    def test_remove_unused_function_template2(self):
        self.check_clang_delta('remove-unused-function/template2.cc', '--transformation=remove-unused-function --counter=1')

    def test_remove_unused_function_unused_funcs(self):
        self.check_clang_delta('remove-unused-function/unused-funcs.cc', '--transformation=remove-unused-function --counter=1')

    def test_remove_unused_var_struct1(self):
        self.check_clang_delta('remove-unused-var/struct1.c', '--transformation=remove-unused-var --counter=1')

    def test_remove_unused_var_struct2(self):
        self.check_clang_delta('remove-unused-var/struct2.c', '--transformation=remove-unused-var --counter=1')

    def test_remove_unused_var_unused_var(self):
        self.check_clang_delta('remove-unused-var/unused_var.cpp', '--transformation=remove-unused-var --counter=1')

    def test_rename_class_base_specifier(self):
        self.check_clang_delta('rename-class/base_specifier.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_bool(self):
        self.check_clang_delta('rename-class/bool.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_class_template(self):
        self.check_clang_delta('rename-class/class_template.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_class_template2(self):
        self.check_clang_delta('rename-class/class_template2.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_dependent(self):
        self.check_clang_delta('rename-class/dependent.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_dependent_name(self):
        self.check_clang_delta('rename-class/dependent_name.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_derive(self):
        self.check_clang_delta('rename-class/derive.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_dtor(self):
        self.check_clang_delta('rename-class/dtor.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_dtor1(self):
        self.check_clang_delta('rename-class/dtor1.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_elaborated_type1(self):
        self.check_clang_delta('rename-class/elaborated_type1.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_elaborated_type2(self):
        self.check_clang_delta('rename-class/elaborated_type2.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_explicit_specialization(self):
        self.check_clang_delta('rename-class/explicit_specialization.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_forward_decl(self):
        self.check_clang_delta('rename-class/forward_decl.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_injected_name(self):
        self.check_clang_delta('rename-class/injected_name.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_instantiation(self):
        self.check_clang_delta('rename-class/instantiation.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_parm(self):
        self.check_clang_delta('rename-class/parm.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_partial_specialization(self):
        self.check_clang_delta('rename-class/partial_specialization.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_rename_class1(self):
        self.check_clang_delta('rename-class/rename-class1.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_rename_class2(self):
        self.check_clang_delta('rename-class/rename-class2.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_specialization(self):
        self.check_clang_delta('rename-class/specialization.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_static_member(self):
        self.check_clang_delta('rename-class/static_member.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_template_class_1(self):
        self.check_clang_delta('rename-class/template_class_1.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_template_parm(self):
        self.check_clang_delta('rename-class/template_parm.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_template_template(self):
        self.check_clang_delta('rename-class/template_template.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_template_template_parm(self):
        self.check_clang_delta('rename-class/template_template_parm.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_typedef(self):
        self.check_clang_delta('rename-class/typedef.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_typedef2(self):
        self.check_clang_delta('rename-class/typedef2.cc', '--transformation=rename-class --counter=1')

    def test_rename_class_using(self):
        self.check_clang_delta('rename-class/using.cpp', '--transformation=rename-class --counter=1')

    def test_rename_class_using1(self):
        self.check_clang_delta('rename-class/using1.cc', '--transformation=rename-class --counter=1')

    def test_rename_cxx_method_overloaded(self):
        self.check_clang_delta('rename-cxx-method/overloaded.cc', '--transformation=rename-cxx-method --counter=1')

    def test_rename_cxx_method_test1(self):
        self.check_clang_delta('rename-cxx-method/test1.cc', '--transformation=rename-cxx-method --counter=1')

    def test_rename_cxx_method_test2(self):
        self.check_clang_delta('rename-cxx-method/test2.cc', '--transformation=rename-cxx-method --counter=1')

    def test_rename_cxx_method_test3(self):
        self.check_clang_delta('rename-cxx-method/test3.cc', '--transformation=rename-cxx-method --counter=1')

    @unittest.skip(reason='Missing rename for last function')
    def test_rename_fun_multi(self):
        self.check_clang_delta('rename-fun/multi.c', '--transformation=rename-fun --counter=1')

    def test_rename_fun_overloaded(self):
        self.check_clang_delta('rename-fun/overloaded.cc', '--transformation=rename-fun --counter=1')

    @unittest.skip(reason='Missing rename for last function')
    def test_rename_fun_test1(self):
        self.check_clang_delta('rename-fun/test1.c', '--transformation=rename-fun --counter=1')

    def test_rename_param_invalid(self):
        self.check_clang_delta('rename-param/invalid.c', '--transformation=rename-param --counter=1')

    def test_rename_var_rename_var(self):
        self.check_clang_delta('rename-var/rename-var.c', '--transformation=rename-var --counter=1')

    def test_replace_derived_class_replace_derived1(self):
        self.check_clang_delta('replace-derived-class/replace-derived1.cpp', '--transformation=replace-derived-class --counter=1')

    def test_replace_derived_class_replace_derived2(self):
        self.check_clang_delta('replace-derived-class/replace-derived2.cpp', '--transformation=replace-derived-class --counter=1')

    def test_replace_derived_class_replace_derived3(self):
        self.check_clang_delta('replace-derived-class/replace-derived3.cpp', '--transformation=replace-derived-class --counter=1')

    def test_replace_derived_class_replace_derived4(self):
        self.check_clang_delta('replace-derived-class/replace-derived4.cpp', '--transformation=replace-derived-class --counter=1')

    def test_replace_function_def_with_decl_macro1(self):
        self.check_clang_delta('replace-function-def-with-decl/macro1.c', '--transformation=replace-function-def-with-decl --counter=1 --to-counter=2')

    def test_replace_function_def_with_decl_macro2(self):
        self.check_clang_delta('replace-function-def-with-decl/macro2.c', '--transformation=replace-function-def-with-decl --counter=1 --to-counter=2')

    def test_return_void_test1(self):
        self.check_clang_delta('return-void/test1.c', '--transformation=return-void --counter=1')

    def test_return_void_test1(self):
        self.check_clang_delta('return-void/test1.cc', '--transformation=return-void --counter=1')

    def test_return_void_test2(self):
        self.check_clang_delta('return-void/test2.c', '--transformation=return-void --counter=1')

    def test_return_void_test3(self):
        self.check_clang_delta('return-void/test3.c', '--transformation=return-void --counter=1')

    def test_return_void_test4(self):
        self.check_clang_delta('return-void/test4.c', '--transformation=return-void --counter=1')

    def test_return_void_test5(self):
        self.check_clang_delta('return-void/test5.c', '--transformation=return-void --counter=1')

    def test_return_void_test6(self):
        self.check_clang_delta('return-void/test6.c', '--transformation=return-void --counter=1')

    def test_simplify_callexpr_macro(self):
        self.check_clang_delta('simplify-callexpr/macro.c', '--transformation=simplify-callexpr --counter=1')

    def test_simplify_callexpr_test(self):
        self.check_clang_delta('simplify-callexpr/test.c', '--transformation=simplify-callexpr --counter=1')

    def test_simplify_callexpr_test2(self):
        self.check_clang_delta('simplify-callexpr/test2.c', '--transformation=simplify-callexpr --counter=1')

    def test_simplify_if_macro(self):
        self.check_clang_delta('simplify-if/macro.c', '--transformation=simplify-if --counter=1')

    def test_union_to_struct_union1(self):
        self.check_clang_delta('union-to-struct/union1.c', '--transformation=union-to-struct --counter=1')

    def test_union_to_struct_union2(self):
        self.check_clang_delta('union-to-struct/union2.c', '--transformation=union-to-struct --counter=1')

    def test_union_to_struct_union3(self):
        self.check_clang_delta('union-to-struct/union3.c', '--transformation=union-to-struct --counter=1')
