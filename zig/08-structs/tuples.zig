const std = @import("std");

// A tuple is an struct without field names.

// The fields are implicitly named using numbers starting from 0. Because
// their names are integers, they cannot be accessed with . syntax without
// also wrapping them in @"". Names inside @"" are always recognised as
// identifiers.

// Like arrays, tuples have a .len field, can be indexed (provided the
// index is comptime-known) and work with the ++ and ** operators. They can
// also be iterated over with inline for.

const Tuple = struct { bool, []const u8, i64 };

const NotTuple = struct { t: bool, e: i32, s: []const u8 };
// common structure provide field names;
// can't be initialized like Tuple, must provide field names.
// NotTuple{ .t = false, .e = 69, .s = "test" };
// doesn't have len field.
// std.debug.print("nt len: {d}\n", .{nt.len}); -> Compile Error

pub fn main() !void {
    const tuple = Tuple{ true, "hi", 1234 };
    printTuple(tuple);
    std.debug.print("{any}\n", .{@TypeOf(tuple)});
    std.debug.print("{d}\n", .{tuple.len});
    std.debug.print("{s}\n", .{tuple[1]});
}

fn printTuple(tuple: Tuple) void {
    inline for (tuple) |val| {
        std.debug.print("{any}\n", .{val});
    }
}
